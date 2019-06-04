package main

import (
	"fmt"
	"os"
	"strconv"
)

func helpMe(errmsg string) int {
	fmt.Println(errmsg)
	fmt.Println()
	s := fmt.Sprintf("Usage:\n\t%s <integer>\n", os.Args[0])
	fmt.Println(s)
	fmt.Println("Calculate sum of even fibonacci values up until")
	fmt.Println("provided max value.")
	return 5
}

func fibonext(a int, b int) (int, int) {
	// fmt.Println("Input: ", a, b) // DEBUG
	a += b
	b += a
	// fmt.Println("Output: ", a, b) // DEBUG
	return a, b
}

func main() {
	if len(os.Args) != 2 {
		os.Exit(helpMe("ERR This takes a single integer as an argument."))
	}
	
	// convert the argument to an integer
	max, _ := strconv.Atoi(os.Args[1])
	value := 0

	// initialize the first two fibonacci values
	x := 1
	y := 2

	for y < max {
		if x%2 == 0 {
			value += x
		}
		
		if y%2 == 0 {
			value += y
		}

		x, y = fibonext(x, y)	
	}

	fmt.Println(value)
}