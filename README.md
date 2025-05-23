# Exploiting and Securing Rolling Code Systems: A Practical Approach to Automotive Cybersecurity

This repository contains the work developed as part of a Master’s thesis in Computer Engineering, carried out within a research and development team specialized in **automotive cybersecurity**. The project focuses on wireless security vulnerabilities in Sub-GHz communication systems commonly used in remote keyless entry (RKE) devices and similar technologies.

The thesis is structured in two main parts:
- **Attack Phase**: Implementation of the RollJam attack, a method theorized by Samy Kamkar and demonstrated at [DefCon](https://samy.pl/defcon2015), which targets rolling code systems by exploiting signal jamming and replay vulnerabilities.
- **Defense Phase**: Design and development of a secure communication protocol based on a challenge-response mechanism, aimed at preventing the vulnerabilities exposed in the first part.

## Abstract

The automotive industry is undergoing a rapid transformation, driven by continuous technological innovation. From the development of autonomous driving systems to the integration of smart electronic components, modern vehicles are becoming increasingly connected and reliant on software-driven systems. This evolution, however, brings with it critical challenges related to cybersecurity.

Cybersecurity has become a key pillar in the design and operation of modern vehicles. From engine control units to infotainment and advanced driver assistance systems, every component is potentially exposed to cyber threats. Among these, **radio-based attacks** on **Sub-GHz communication protocols** remain significantly underestimated, despite their effectiveness and potential impact.

Such attacks are not limited to the automotive sector; they also affect devices like alarm systems, garage doors, and other IoT systems operating on similar frequencies. This thesis explores one of the most effective techniques — the RollJam attack — and demonstrates its feasibility in real-world scenarios.

In response to this vulnerability, the project proposes and implements a **secure challenge-response protocol**, designed to protect against replay and jamming attacks. The result is a robust and practical solution to enhance the security of wireless access systems.

## Folders

> + [Challenge_Response_Security](https://github.com/filippoveronesi/rolling_code_attack_challenge_response_solution/tree/main/Challenge_Response_Security): Python-based implementation of the defensive protocol  
> + [Rolling_Jamming_Attack](https://github.com/filippoveronesi/rolling_code_attack_challenge_response_solution/tree/main/Rolling_Jamming_Attack): Practical implementation of the RollJam attack targeting automotive remote keys  
> + [Video_Test](https://github.com/filippoveronesi/rolling_code_attack_challenge_response_solution/tree/main/Video_Test): Video demonstrations of both the attack and the defense mechanisms

## Rolling_Jamming_Attack

<p align="center">
  <img src="https://github.com/filippoveronesi/rolling_code_attack_challenge_response_solution/blob/main/Rolling_Jamming_Attack/img/rolljam-diagram.png" alt="rolljam"/>
</p>

## Challenge_Response_Security

<p align="center">
  <img src="https://github.com/filippoveronesi/rolling_code_attack_challenge_response_solution/blob/main/Challenge_Response_Security/img/protocol.png" alt="defense protocol"/>
</p>