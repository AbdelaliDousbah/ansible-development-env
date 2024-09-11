Vagrant.configure("2") do |config|
  # Ubuntu 20.04 VM
  config.vm.define "ubuntu_vm" do |ubuntu|
    ubuntu.vm.box = "generic/ubuntu2004"

    ubuntu.vm.provider "libvirt" do |v|
      v.memory = 1024
      v.cpus = 1
    end
  end

  # CentOS 8 VM
  config.vm.define "centos_vm" do |centos|
    centos.vm.box = "generic/centos8"

    centos.vm.provider "libvirt" do |v|
      v.memory = 1024
      v.cpus = 1
    end
  end
end
