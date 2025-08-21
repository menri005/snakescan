# SnakeScan

> ROY CAMPBELL: As usual, this is a one-man infiltration mission.
>
> SOLID SNAKE: Weapons and equipment OSP (on-site procurement)?
>
> ROY CAMPBELL: Yes. This is a top-secret black op. Don't expect any official support.
>> Metal Gear Solid

Have you ever landed a shell on a host, and your typical pivoting techniques (proxychains, Metasploit, etc.) aren't working? Does this host have Python installed in it? If so, you've come to the right place.

A fast and flexible Python network scanner, **SnakeScan**, can scan single hosts or entire subnets. Supports **individual ports, port ranges, or a mix of both**, and can export results to a CSV file. Best of all, it uses **standard** libraries, so no need to install dependencies.

---

## **Features**

- Scan a **single host** or a **subnet** (CIDR notation, e.g., `192.168.1.0/24`)  
- Specify ports as:
  - Individual ports: `22,80,443`  
  - Ranges: `8000-8080`  
  - Mixed: `22,80,443,8000-8080`  
- Multi-threaded scanning for speed  
- Export results to a CSV file  
- Works on Python 3  

---

## **Requirements**

- Python 3.x  
- No additional libraries (uses standard library modules: `socket`, `argparse`, `concurrent.futures`, `ipaddress`, `csv`)

---

## **Usage**

```bash
python3 port_scanner.py -t TARGET [-p PORTS]
```

This will create a CSV named `results.csv` after the scan is done. 

---

## Author
Martin Enriquez
tuxedo.netcat@gmail.com
https://github.com/menri005
