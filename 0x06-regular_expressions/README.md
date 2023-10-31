# 0x06. Regular expression

## Background Context

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the `//`:

```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

0. Simply matching School
	<img width="969" alt="regex_task1" src="https://github.com/Abucheri/alx-system_engineering-devops/assets/24778489/13b8dd33-238c-4bc6-86e9-142b01ea0d17">
 	- Requirements:
		- The regular expression must match `School`
		- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
	- Example:
	```
	sylvain@ubuntu$ ./0-simply_match_school.rb School | cat -e
	School$
	sylvain@ubuntu$ ./0-simply_match_school.rb "Best School" | cat -e
	School$
	sylvain@ubuntu$ ./0-simply_match_school.rb "School Best School" | cat -e
	SchoolSchool$
	sylvain@ubuntu$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
	$
	```

1. Repetition Token #0
	<img width="959" alt="regex_task2" src="https://github.com/Abucheri/alx-system_engineering-devops/assets/24778489/667fb407-5e88-41cd-bb83-a491f32f4c5f">
	- Requirements:
		- Find the regular expression that will match the above cases
		- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

2. Repetition Token #1
	
	- Requirements:
		- Find the regular expression that will match the above cases
		- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
