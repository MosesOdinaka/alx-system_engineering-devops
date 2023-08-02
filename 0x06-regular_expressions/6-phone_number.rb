#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: #($0) <phone_number>"
  exit
end

input = ARGV[0]
pattern = /^\d{10,10}$/

if input.match(pattern)
  puts input
end
