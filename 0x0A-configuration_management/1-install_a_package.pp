# A Puppet manifest that installs Flask version 2.1.0 using pip3.

exec { 'Flask':
    command => 'sudo pip3 install Flask==2.1.0',
    path    => '/usr/bin:/usr/sbin:/bin',
}
