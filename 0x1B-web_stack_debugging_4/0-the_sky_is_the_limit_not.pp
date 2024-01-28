# Increase the request limit in Nginx configuration

exec { 'increase_nginx_request_limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart the Nginx service to apply the changes
-> exec { 'restart_nginx_service':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
