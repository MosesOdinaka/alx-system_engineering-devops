# Modify the hard limit for the 'holberton' user
exec { 'modify_hard_limit':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Modify the soft limit for the 'holberton' user
exec { 'modify_soft_limit':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
