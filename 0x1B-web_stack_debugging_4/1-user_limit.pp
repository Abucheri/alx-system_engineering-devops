# Puppet manifest to change OS configuration for holberton user

# Set open files limit for holberton user
limits { 'holberton_open_files':
  ensure   => 'present',
  domain   => 'holberton',
  type     => 'hard',
  item     => 'nofile',
  value    => '4096',
  apply_to => 'all',
  provider => 'pam',
}
