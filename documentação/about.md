# Introdução

Tiny Machine Learning (TinyML) é uma tecnologia emergente proposta pela comunidade científica para o desenvolvimento de dispositivos embarcados focados em autonomia e segurança. Seu objetivo é embarcar modelos de Aprendizado de Máquina (Machine Learning - ML) e Redes Neurais (Neural Networks - NNs) em hardwares com recursos limitados, capazes de processar dados localmente. A tecnologia busca democratizar a Inteligência Artificial (IA) através da isenção de uma infraestrutura robusta e onerosa para processamento massivo de dados, tornando-a acessível a mais setores e contribuindo para a revolução digital dos dispositivos inteligentes[1][2].

O crescimento massivo da Internet das Coisas (IoT) e da computação de borda (edge computing) impulsionou a necessidade de integrar capacidades de ML em dispositivos embarcados. Tradicionalmente, os sistemas de IoT enviam dados brutos para a nuvem para processamento e análise[3]. No entanto, essa abordagem apresenta desvantagens significativas[4].

Por mais autonomia que o TinyML possa proporcionar, ter uma infraestrutura que possibilite notificações e monitoramento dos dados gerados pelos dispositivos é essencial. Principalmente quando levado em consideração que, aplicações típicas de IoT utilizam dezenas, centenas e até milhares desses dispositivos[5]. Este projeto tem como foco a implementação de uma infraestrutura distribuída para TinyML, utilizando Docker Swarm para gerenciamento, MQTT para notificação dos dispositivos, um banco de dados para persistência e ThingsBoard para visualização. Esta estrutura busca criar um ecossistema robusto que suporte o ciclo de vida dos dados e das decisões tomadas pelos dispositivos TinyML na borda.

<br><br>

# Problema a ser tratado

Sistemas tradicionais de Machine Learning, especialmente Deep Learning (DL), exigem recursos computacionais substanciais, frequentemente confinados a estações de trabalho poderosas ou infraestruturas de nuvem. Embora essa abordagem seja eficaz para tarefas complexas, ela impõe barreiras significativas para a implantação de ML em milhões de dispositivos IoT e embarcados, que são inerentemente restritos em termos de capacidade de processamento, memória e energia.

<br><br>

# Jusrificativa

Existem alguns pontos de benefícios ao se implementar uma infraestrutura de suporte a dispositivos TinyML em comparação com os sistemas tradicionais baseados em nuvem. Ao processar dados no dispositivo, a latência de decisão é drasticamente reduzida, permitindo respostas quase instantâneas. Dados sensíveis podem ser processados localmente, reduzindo ou eliminando a necessidade de transmiti-los pela rede, mitigando assim os riscos de privacidade e segurança. Com a necessidade de transmissão de dados reduzida tem-se um menor consumo de energia, prolongando a vida útil da bateria dos dispositivos. A capacidade de operar offline ou com conectividade limitada aumenta a robustez e a confiabilidade do sistema em ambientes desafiadores[2][3].

O TinyML tem aplicações em diversas áreas, como manutenção preditiva (PdM), saúde, agricultura e segurança[4]. A combinação com uma infraestrutura distribuída gera um ecossistema robusto, monitorável e escalável.

O interesse em TinyML vem gerando soluções em diversas áreas, como a Imagimob, empresa sueca que criou uma plataforma para desenvolvimento de soluções com inteligência artificial na borda para pecuária e agrícola.[6]

Outro exemplo é a Elogix-Ping que utiliza o TinyML para monitorar a assinatura acústica de pás de turbinas eólicas, tornando possível fazer manutenções preventivas mais acertadas e identificar alterações e danos.[7]

A principal plataforma para desenvolvimento TinyML é o TensorFlow Lite do Google. Diversas empresas de hardware vem desenvolvendo placas voltadas para aplicações de IA de borda como a Arduino, SparkFun, Espressif, Nordic entre outras.[8]

<br><br>

# Objetivos

## Objetivo Geral

- Implementar uma infraestrutura distribuída escalável para aplicações de TinyML, integrando dispositivos de borda com recursos restritos a um backend de gerenciamento, comunicação e visualização baseado em Docker Swarm, MQTT, banco de dados e ThingsBoard.

## Objetivos Específicos

- Implementar e gerenciar os serviços de backend (broker MQTT, banco de dados, ThingsBoard) de forma distribuída e resiliente utilizando Docker Swarm.
- Configurar o ThingsBoard para capturar dados, representar os dispositivos TinyML e criar dashboards para visualização e monitoramento.
- Simular o comportamento de múltiplos dispositivos TinyML para testar a escalabilidade e o desempenho da infraestrutura distribuída.

<br><br>

# Referências Bibliográficas

[1] Tsoukas, V., Gkogkidis, A., Boumpa, E., e Kakarountas, A. (2024) **A Review on the emerging technology of TinyML.** ACM Comput. Surv., Vol. 56, No. 10, Article 259.

[2] Kallimani, R., Pai, K., Raghuwanshi, P., Iyer, S., e López, O. L. A. (2023) **TinyML: Tools, applications, challenges, and future research directions.** Multimedia Tools and Applications (2024).

[3] Elhanashi, A., Dini, P., Saponara, S., e Zheng, Q. (2024) **Advancements in TinyML: Applications, Limitations, and Impact on IoT Devices.** MDPI Electronics 2024.

[4] Njor, E., Hasanpour, M. A., Madsen, J., e Fafoutis, X. (2024) **A Holistic Review of the TinyML Stack for Predictive Maintenance.** IEEE Access

[5] Dusun. **How Many Devices Can An IoT Gateway Connect? A Complete Guide in 2024.** Blog Dusun, 2024. Disponível em: [https://www.dusuniot.com/blog/how-many-devices-can-an-iot-gateway-connect/](https://www.dusuniot.com/blog/how-many-devices-can-an-iot-gateway-connect/)

[6] Imagimob. [https://www.imagimob.com/](https://www.imagimob.com/)

[7] Elogix-ping. [https://eologix-ping.com/en](https://eologix-ping.com/en)

[8] LiteRT for Microcontrollers. [https://ai.google.dev/edge/litert/microcontrollers/overview](https://ai.google.dev/edge/litert/microcontrollers/overview) 