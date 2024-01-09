# 2-puppet_custom_http_response_header.pp
# Puppet manifest to configure Nginx with a custom HTTP response header

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

package { 'nginx':
  ensure => present,
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {\n    add_header X-Served-By ${hostname};\n}\n",
  require => Package['nginx'],
}

file { '/etc/nginx/sites-enabled/00-custom':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/00-custom'],
}
