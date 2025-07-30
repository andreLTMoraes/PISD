#!/bin/bash
if command docker -v &> /dev/null; then
    echo "Docker is already installed."
else
    echo "Instalando o Docker..."
    curl -fsSL https://get.docker.com | sudo bash
    echo "Docker instalado!!!"
    echo "Instalando o compose..."
    sudo curl -fsSL "https://github.com/docker/compose/releases/download/v2.39.1/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    echo "compose instalado!!!"
    sudo usermod -aG docker vagrant
    echo "Permissão para o usuário 'vagrant' concedida!!!"
fi
