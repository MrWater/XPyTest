"""
generate_anchors.py
"""
import numpy as np

# Verify that we compute the same anchors as Shaoqing's matlab implementation:
#
#    >> load output/rpn_cachedir/faster_rcnn_VOC2007_ZF_stage1_rpn/anchors.mat
#    >> anchors
#
#    anchors =
#
#       -83   -39   100    56
#      -175   -87   192   104
#      -359  -183   376   200
#       -55   -55    72    72
#      -119  -119   136   136
#      -247  -247   264   264
#       -35   -79    52    96
#       -79  -167    96   184
#      -167  -343   184   360

# array([[ -83.,  -39.,  100.,   56.],
#        [-175.,  -87.,  192.,  104.],
#        [-359., -183.,  376.,  200.],
#        [ -55.,  -55.,   72.,   72.],
#        [-119., -119.,  136.,  136.],
#        [-247., -247.,  264.,  264.],
#        [ -35.,  -79.,   52.,   96.],
#        [ -79., -167.,   96.,  184.],
#        [-167., -343.,  184.,  360.]])


def generate_anchors(stride=16, sizes=(32, 64, 128, 256, 512), aspect_ratios=(0.5, 1, 2)):
    """
    生成 anchor boxes 矩阵，其格式为 (x1, y1, x2, y2).
    Anchors 是以 stride / 2 的中心，逼近指定大小的平方根面积(sqrt areas),长宽比
    Anchors are centered on stride / 2, have (approximate) sqrt areas of the specified
    sizes, and aspect ratios as given.
    """
    return _generate_anchors(stride,
                             np.array(sizes, dtype=np.float) / stride,
                             np.array(aspect_ratios, dtype=np.float) )


def _generate_anchors(base_size, scales, aspect_ratios):
    """
    通过枚举关于参考窗口window (0, 0, base_size - 1, base_size - 1) 的长宽比(aspect ratios) X scales，
    来生成 anchore 窗口(参考窗口 reference windows).
    """
    anchor = np.array([1, 1, base_size, base_size], dtype=np.float) - 1
    anchors = _ratio_enum(anchor, aspect_ratios)
    anchors = np.vstack([_scale_enum(anchors[i, :], scales) for i in range(anchors.shape[0])])
    return anchors


def _whctrs(anchor):
    """
    返回 anchor 窗口的 width, height, x center,  y center.
    """
    w = anchor[2] - anchor[0] + 1
    h = anchor[3] - anchor[1] + 1
    x_ctr = anchor[0] + 0.5 * (w - 1)
    y_ctr = anchor[1] + 0.5 * (h - 1)
    return w, h, x_ctr, y_ctr


def _mkanchors(ws, hs, x_ctr, y_ctr):
    """
    给定 center(x_ctr, y_ctr) 及 widths (ws)，heights (hs) 向量，输出 anchors窗口window 集合.
    """
    ws = ws[:, np.newaxis]
    hs = hs[:, np.newaxis]
    anchors = np.hstack( (x_ctr - 0.5 * (ws - 1), y_ctr - 0.5 * (hs - 1),
                          x_ctr + 0.5 * (ws - 1), y_ctr + 0.5 * (hs - 1) ) )
    return anchors


def _ratio_enum(anchor, ratios):
    """
    对于每个关于一个 anchor 的长宽比aspect ratio，枚举 anchors 集合.
    """
    w, h, x_ctr, y_ctr = _whctrs(anchor)
    size = w * h
    size_ratios = size / ratios
    ws = np.round(np.sqrt(size_ratios))
    hs = np.round(ws * ratios)
    anchors = _mkanchors(ws, hs, x_ctr, y_ctr)
    return anchors


def _scale_enum(anchor, scales):
    """
    对于每个关于一个 anchor 的尺度scale，枚举 anchors 集合.
    Enumerate a set of anchors for each scale wrt an anchor."""
    w, h, x_ctr, y_ctr = _whctrs(anchor)
    ws = w * scales
    hs = h * scales
    anchors = _mkanchors(ws, hs, x_ctr, y_ctr)
    return anchors


if __name__ == '__main__':
    print('Anchor Generating ...')

    anchors = generate_anchors()
    print(anchors)

    print('Done.')
