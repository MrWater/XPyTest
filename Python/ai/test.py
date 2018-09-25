import numpy as np
import pycuda.autoinit
import pycuda.driver as cuda
from pycuda.compiler import SourceModule
mod = SourceModule('''
__global__ void Text_GPU(float *A , float *B){
 
    int bid = blockIdx.x;  
    int tid = threadIdx.x;
 
    __shared__ float s_data[128];
 
    s_data[tid] = A[bid*128 + tid];
    __syncthreads();
 
    for(int i = 64;i>0;i/=2){
        if(tid < i)
            s_data[tid] = s_data[tid] + s_data[tid +i];
        __syncthreads();
    }
    if(tid == 0)
        B[bid] = s_data[0];
 
}
''')
Text_GPU = mod.get_function("Text_GPU")
A = np.ones((32, 128), dtype=np.float32)
B = np.ones((32,), dtype=np.float32)
Text_GPU(cuda.In(A), cuda.InOut(B), grid=(32, 1), block=(128, 1, 1))
print(B)
