#install flask
#version must be 2.1.0

exec { 'install flask':
command => 'pip3 install Flask==2.1.0',
path 	=> ['/usr/bin/'],
unless  => '/usr/bin/test -f /usr/local/lib/python2.1.0/dist-packages/flask/app.py',
}
