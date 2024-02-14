# 0-strace_is_your_friend.pp
# Puppet manifest to fix Apache 500 error related to permissions

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
