machines = {
  "master" => {"memory" => "512", "cpu" => "1", "ip" => "100", "image" => "picassodigital/ubuntu-24.04"},
  "node01" => {"memory" => "512", "cpu" => "1", "ip" => "101", "image" => "picassodigital/ubuntu-24.04"},
  "node02" => {"memory" => "512", "cpu" => "1", "ip" => "102", "image" => "picassodigital/ubuntu-24.04"}
}

Vagrant.configure("2") do |config|

  machines.each do |name, conf|
    config.vm.define "#{name}" do |machine|
      machine.vm.box = "#{conf["image"]}"
      machine.vm.hostname = "#{name}"
      machine.vm.network "private_network", ip: "10.10.10.#{conf["ip"]}"
      config.vm.network "forwarded_port", guest: 8080, host: 8080, host_ip: "0.0.0.0", auto_correct: true
      config.vm.network "forwarded_port", guest: 8888, host: 8888, host_ip: "0.0.0.0"
      config.vm.network "forwarded_port", guest: 1883, host: 1883, host_ip: "0.0.0.0"
      config.vm.usable_port_range = (8000..8100)
      machine.vm.boot_timeout = 600
      machine.vm.provider "virtualbox" do |vb|
        vb.name = "#{name}"
        vb.memory = conf["memory"]
        vb.cpus = conf["cpu"]
        
      end
      machine.vm.provision "shell", path: "installDocker.sh"
      
      if "#{name}" == "master"
        machine.vm.provision "shell", path: "masterSwarm.sh"
      else
        machine.vm.provision "shell", path: "workerSwarm.sh"
      end

    end
  end
end