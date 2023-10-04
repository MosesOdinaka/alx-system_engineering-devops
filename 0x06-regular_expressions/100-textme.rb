#!/usr/bin/env ruby
input = ARGV[0]
from = input.scan(/from:(\+?\w+)/).flatten.first
to = input.scan(/to:(\+?\w+)/).flatten.first
flags = input.scan(/flags:(\S+)/).flatten.first
puts "#{from},#{to},#{flags}"