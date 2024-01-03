# File: 7-puppet_install_nginx_web_server.pp
# Ensure Nginx is installed
# Create a simple HTML page
# Configure Nginx
# Create a custom 404 page
# Set up a redirect for /redirect_me
# Ensure Nginx service is running and enabled
include stdlib

$redirect_link = 'https://www.youtube.com/watch?v=QH2-TGUlwu4'
$page_content = "\trewrite ^/redirect_me/$ ${redirect_link} permanent;"

exec { 'update packages':
  command => '/usr/bin/apt-get update'
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
  require => Package['nginx']
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update packages']
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
  mode    => '0644',
  owner   => 'root',
  group   => 'root'
}

file_line { 'Set 301 redirection':
  ensure   => 'present',
  after    => 'server_name\ _;',
  path     => '/etc/nginx/sites-available/default',
  multiple => true,
  line     => $page_content,
  notify   => Exec['restart nginx'],
  require  => File['/var/www/html/index.html']
}
