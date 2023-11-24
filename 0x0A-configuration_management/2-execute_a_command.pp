# A Puppet manifest that to kill a process

exec { 'kill_process':
    command => 'pkill -f killmenow',
    path    => '/usr/bin:/usr/sbin:/bin',
}
