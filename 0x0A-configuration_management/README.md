# 0x0A-configuration_management
DevOps
SysAdmin
Scripting
CI/CD

## Resources
- Intro to Configuration Management
- Puppet resource type: file (check “Resource types” for all manifest types in the left menu)
- Puppet’s Declarative Language: Modeling Instead of Scripting
- Puppet lint
- Puppet emacs mode

## Requirements
- All your files will be interpreted on Ubuntu 20.04 LTS

## Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

## Install puppet
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades

$ apt-get install -y ruby-augeas

$ apt-get install -y ruby-shadow

$ apt-get install -y puppet

## Tasks
**0. Create a file**

Using Puppet, create a file in /tmp.

**1. Install a package**

Using Puppet, install flask from pip3.

**2. Execute a command**

Using Puppet, create a manifest that kills a process named killmenow.