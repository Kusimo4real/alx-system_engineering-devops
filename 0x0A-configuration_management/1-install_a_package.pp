#install flask
#version must be 2.1.0

exec { 'install flask':
command => 'pip3 install flask==2.1.0',
path    => '/usr/bin/',
unless  => 'pip3 list | grep flask',
}
