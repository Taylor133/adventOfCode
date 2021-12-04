package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("./input/day3TestInput.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	part2(scanner)

	// optionally, resize scanner's capacity for lines over 64K, see next example

}

func getMostPopularValue(data []int) int {
	mostPopular := 0
	for j := 0; j < len(data); j++ {
		if data[j] == 0 {
			mostPopular -= 1
		} else {
			mostPopular += 1
		}
	}
	if mostPopular > 0 {
		return 1
	} else {
		return 0
	}
}

func part1(scanner *bufio.Scanner) int {
	arr := make([][]int, 0)

	for scanner.Scan() {
		if len(arr) == 0 {
			for j := 0; j < len(scanner.Text()); j++ {
				arr = append(arr, make([]int, 0))
			}
		}
		//fmt.Println(arr)
		for i := 0; i < len(scanner.Text()); i++ {
			//fmt.Println((scanner.Text()[i : i+1]))
			if n, err := strconv.Atoi(scanner.Text()[i : i+1]); err == nil {

				arr[i] = append(arr[i], n)
			}
		}
		//arr = append(arr, scanner.Text())
	}
	//fmt.Println(arr)

	gammaValue, epsilonValue := "", ""
	for i := 0; i < len(arr); i++ {
		mostPopular := getMostPopularValue(arr[i])
		if mostPopular == 0 {
			gammaValue += "1"
			epsilonValue += "0"
		} else {
			epsilonValue += "1"
			gammaValue += "0"
		}
	}
	gammaDec, err := strconv.ParseInt(gammaValue, 2, 64)
	if err != nil {
		fmt.Println(err)
		return 0
	}
	epsilonDec, err := strconv.ParseInt(epsilonValue, 2, 64)
	if err != nil {
		fmt.Println(err)
		return 0
	}
	fmt.Println(gammaDec)
	fmt.Println(epsilonDec)
	return int(gammaDec * epsilonDec)
}

func part2(scanner *bufio.Scanner) int {

	data := make([]string, 0)
	for scanner.Scan() {
		data = append(data, scanner.Text())
	}
	//fmt.Println(data)

	oxygenData := data
	fmt.Println(oxygenData)

	for i := 0; i < 5; i++ {
		arr := make([][]int, 0)

		for j := 0; j < len(oxygenData); j++ {
			if len(arr) == 0 {
				fmt.Println("new")
				for l := 0; l < len(oxygenData[j]); l++ {
					arr = append(arr, make([]int, 0))
				}
			}
			for k := 0; k < len(oxygenData[j]); k++ {
				n, err := strconv.Atoi(oxygenData[j][k : k+1])
				if err != nil {
					fmt.Println(err)
					return 0
				}
				arr[k] = append(arr[k], n)
			}
		}
		fmt.Println(arr)
	}

	return 0
}
