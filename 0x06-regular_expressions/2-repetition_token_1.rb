#!/usr/bin/env ruby

if ARGV.length != 1
    puts "Usage: #{$0} <string>"
    exit
  end
  
  input = ARGV[0]
  pattern = /hb?t?n/
  
  matches = input.scan(pattern)
  puts matches.join