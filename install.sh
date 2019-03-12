#!/usr/bin/env bash

main(){
  # Create fup directory
  mkdir fup

  # Create fup script
  echo "#!/usr/bin/env bash

help(){
  curl http://josegalarza.pythonanywhere.com/help
}

# If not 1 parameter
if [ "\$\#" != 1 ]; then
  # Missing parameter
  help
else
  # If parameter is file
  if [ -f \$1 ]; then
  	# Upload file
  	curl http://josegalarza.pythonanywhere.com -F file=@\$1
  else
  	# Download from hash
    curl http://josegalarza.pythonanywhere.com/\$1
  fi
fi
" > fup/fup

  # Make it executable
  chmod +x fup/fup

  # Add it to PATH
  # echo "export PATH=\$PATH:\$(pwd)/fup" >> ~/.bashrc
  echo PATH=\$PATH:$(pwd)/fup

  # Reload ~/.bashrc
  source ~/.bashrc
}

main
