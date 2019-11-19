FROM energy/rapl:1

ENV BINARY=/usr/bin/ravi
COPY . .

RUN apk add cmake llvm git gcc g++ ccache &&\
    git clone https://github.com/dibyendumajumdar/ravi.git /tmp/ravi &&\
    cd /tmp/ravi &&\
    cmake \
        -D CMAKE_MAKE_PROGRAM=/usr/bin/cmake \
        -D CMAKE_C_COMPILER=/usr/bin/gcc \
        -D CMAKE_CXX_COMPILER=/usr/bin/g++ \
        -D CMAKE_BUILD_TYPE=Release \
        -D LLVM_JIT=ON \
        -D CMAKE_INSTALL_PREFIX=/opt/ravi \
        -D LLVM_DIR=/opt/llvm801/lib/cmake/llvm .
RUN /usr/bin/python3 compile_all.py compile
