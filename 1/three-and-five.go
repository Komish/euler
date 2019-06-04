package main

import (
	"fmt"
	"os"
	"strconv" 	// the command line args give us a string
			  	// but we need an integer
)

func isMultiple(this int, that int) bool {
	state := false
	if that%this == 0 {
		state = true
	}
	return state
}

func helpMe(errmsg string) int {
	fmt.Println(errmsg)
	fmt.Println("Usage:")
	fmt.Printf("%s integer\n", os.Args[0])
	fmt.Printf("Display sum of multiples of 3 and 5")
	fmt.Printf(" between 1 to the specified integer\n")
	return 5
}

func main() {
	if len(os.Args) != 2 {
		os.Exit(helpMe("ERR This takes a single integer as an argument"))
	}
	counter, _ := strconv.Atoi(os.Args[1])
	res := 0
	for i :=1 ; i < counter ; i ++ {
		if ( isMultiple(3, i) || isMultiple(5, i) ) {
			res += i
		}
	}
	fmt.Println(res)
}