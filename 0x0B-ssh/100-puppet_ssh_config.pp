#!/usr/bin/env bash
# making configuration changes using puppet.

file { 'ect/ssh/ssh_config':
	ensure => present,

content =>"
	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
}

