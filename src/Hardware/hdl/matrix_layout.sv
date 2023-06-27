module matrix_layout #(parameter DATA_WIDTH = 32,
                                    MAX_ROWS = 2,
                                    MAX_COLS = 2
    )(
        input logic  [DATA_WIDTH-1:0] matrix_A [MAX_ROWS-1:0][MAX_COLS-1:0] ,
        input logic  [DATA_WIDTH-1:0] matrix_B [MAX_ROWS-1:0][MAX_COLS-1:0] ,
        output logic [DATA_WIDTH-1:0] matrix_C [MAX_ROWS-1:0][MAX_COLS-1:0]
    );

  //2x2 Matrix Multiplication
  always_comb begin : MatrixCalculation
    matrix_C[0][0] = (matrix_A[0][0] * matrix_B[0][0]) + (matrix_A[0][1] * matrix_B[1][0]);
    matrix_C[0][1] = (matrix_A[0][0] * matrix_B[0][1]) + (matrix_A[0][1] * matrix_B[1][1]);
    matrix_C[1][0] = (matrix_A[1][0] * matrix_B[0][0]) + (matrix_A[1][1] * matrix_B[1][0]);
    matrix_C[1][1] = (matrix_A[1][0] * matrix_B[0][1]) + (matrix_A[1][1] * matrix_B[1][1]);
  end
  
endmodule