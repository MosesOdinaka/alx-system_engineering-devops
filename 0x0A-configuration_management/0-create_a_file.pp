# This is a Puppet manifest designed to generate a file at /tmp/school,
# complete with specified permissions, owner, group, and content.

file { '/tmp/school':
    ensure  => 'file',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet\n'
}
