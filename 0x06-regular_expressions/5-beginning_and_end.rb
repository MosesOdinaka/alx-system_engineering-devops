#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: #($0) <string>"
  exit
end

input = ARGV[0]
pattern = /^h.n$/

if imput.match(pattern)
  puts input
end
