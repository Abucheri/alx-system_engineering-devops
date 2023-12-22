# Puppet Manifest: 2-execute_a_command.pp
# Description: Terminate a process named "killmenow" using pkill

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => '/usr/bin/pgrep killmenow',
}
