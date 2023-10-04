#!/usr/bin/env ruby

if ARGV.length != 1
    puts "Usage: #($0) <string>"
    exit
  end
  
  input = ARGV[0]
  pattern = /hbt{2,5}n/
  
  matches = input.scan(pattern)
  puts matches.join