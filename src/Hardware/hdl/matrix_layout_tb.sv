
`timescale 1ns/1ns

module matrix_layout_tb;
	
	logic clk;
	logic [31:0] matrix_A [1:0][1:0];
	logic [31:0] matrix_B [1:0][1:0];
	logic [31:0] matrix_C [1:0][1:0];
	
	matrix_layout #(32, 2, 2) dut (
		.matrix_A(matrix_A),
		.matrix_B(matrix_B),
		.matrix_C(matrix_C)
	);	

	initial begin
		matrix_A <= '{'{1,0},
			     '{0,1}}; #10;
		matrix_B <= '{'{1,2},
			     '{3,4}}; #10;
	end
	
	always begin
		#5;
		clk <= ~clk;
	end
	
	initial begin
		clk <= 0;
		#1; // Wait for a short duration before starting the simulation
		$monitor("Time=%0t A=%p B=%p C=%p", $time, matrix_A, matrix_B, matrix_C);
		#30; // Simulation duration
		$finish;
	end
endmodule