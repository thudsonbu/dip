package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	str := "01001000 01101001 00100000 01101000 01100101 01101100 01101100 01101111 00100000 01101001 01100110 00100000 01111001 01101111 01110101 00100000 01100001 01110010 01100101 00100000 01110010 01100101 01100001 01100100 01101001 01101110 01100111 00100000 01110100 01101000 01101001 01110011 00100000 01110111 01100101 00100000 01101000 01101111 01110000 01100101 00100000 01110011 01101111 01101101 01100101 01110100 01101000 01101001 01101110 01100111 00100000 01100111 01101111 01101111 01100100 00100000 01101000 01100001 01110000 01110000 01100101 01101110 01110011 00100000 01110100 01101111 00100000 01111001 01101111 01110101 00100000 01101001 01101110 00100000 00110010 00110000 00110010 00110011 00101110"

	strArr := strings.Split(str, " ")

	for _, v := range strArr {
		i := convertBinaryStrToInt(v)
		fmt.Print(string(i))
	}
}

func convertBinaryStrToInt(binStr string) int {
	num, err := strconv.ParseInt(binStr, 2, 64)

	if err != nil {
		fmt.Println(err)
		return 0
	}

	return int(num)
}
