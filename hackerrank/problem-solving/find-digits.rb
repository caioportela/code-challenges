#!/bin/ruby

require 'json'
require 'stringio'

def findDigits(n)
    number = n
    count = 0

    while number > 0 do
        digit = number % 10
        number /= 10
        
        count += 1 if digit != 0 and n % digit == 0
    end

    return count
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

t = gets.to_i

t.times do |t_itr|
    n = gets.to_i

    result = findDigits n

    fptr.write result
    fptr.write "\n"
end

fptr.close()
