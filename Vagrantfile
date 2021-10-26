# -*- mode: ruby -*-
# vi: set ft=ruby :

$start = <<SCRIPT
#!/usr/bin/env bash

export LC_ALL=C
export DEBIAN_FRONTEND=noninteractive 

apt-get update && apt-get install -yy --no-install-recommends docker docker-compose

cd /vagrant

docker-compose pull
docker-compose build
docker-compose up -d

SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  config.vm.network "forwarded_port", guest: 5050, host: 5050
  config.vm.network "forwarded_port", guest: 5150, host: 5100
  config.vm.network "forwarded_port", guest: 8080, host: 8080

  config.vm.provision :shell, inline: $start, run: "always"

  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 2
  end
end
