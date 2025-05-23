# rolling_code_attack_challenge_response_solution

This project is divided into two main parts:  
- **Attack Phase**: Implementation of the RollJam attack, a vulnerability theorized by Samy Kamkar at [DefCon](https://samy.pl/defcon2015).  
- **Defense Phase**: Development of a countermeasure through a secure challenge-response protocol.

## Abstract

The automotive industry is undergoing rapid transformation, driven by technological innovation that is making vehicles increasingly intelligent and connected. From the push toward autonomous driving to the integration of advanced electronics, modern vehicles depend heavily on digital systems. This evolution brings with it critical cybersecurity challenges.

Cybersecurity has become a foundational element in automotive design. Today’s vehicles include interconnected systems for everything from engine control to infotainment and assisted driving. While this connectivity offers improved comfort and safety, it also increases exposure to potential cyber threats.

Among the most underestimated threats are **radio-based attacks**, particularly those using **Sub-GHz frequencies**. These attacks are powerful and can compromise a wide range of devices, including not just vehicles, but also alarms, gates, and other systems using similar wireless communication.

This thesis explores a practical implementation of such an attack — the RollJam technique — and demonstrates its feasibility and impact. The work aims to highlight the risks associated with Sub-GHz radio attacks and show the need for stronger, more secure access control mechanisms.

In the second part of the project, an **innovative defensive protocol** is proposed. Based on a challenge-response mechanism, this protocol enhances the security of access systems by preventing replay and jamming-based attacks.

## Folders

> + [Challenge_Response_Security](https://github.com/filippoveronesi/rolling_code_attack_challenge_response_solution/tree/main/Challenge_Response_Security): Python-based defensive solution  
> + [Rolling_Jamming_Attack](https://github.com/filippoveronesi/rolling_code_attack_challenge_response_solution/tree/main/Rolling_Jamming_Attack): RollJam attack implementation targeting automotive remote keys  
> + [Video_Test](https://github.com/filippoveronesi/rolling_code_attack_challenge_response_solution/tree/main/Video_Test): Demonstration videos of both attack and defense phases

## Rolling_Jamming_Attack

<p align="center">
  <img src="https://github.com/filippoveronesi/rolling_code_attack_challenge_response_solution/blob/main/Rolling_Jamming_Attack/img/rolljam-diagram.png" alt="rolljam"/>
</p>

## Challenge_Response_Security

<p align="center">
  <img src="https://github.com/filippoveronesi/rolling_code_attack_challenge_response_solution/blob/main/Challenge_Response_Security/img/protocol.png" alt="def"/>
</p>