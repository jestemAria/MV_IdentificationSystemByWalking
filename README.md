# MV_IdentificationSystemByWalking

This project is a system focused on the identification of the human body by walking.
It is based on machine vision concepts and algorithms.
------

### System Schematic
```mermaid
graph LR
A((Built-in Camera)) -- OpenCV --> B[Median Mask]
B --> C[Canny Edge Detection]
C --> D{Final Result}
```

### TODO:
- [ ] Segmenation of the body.
- [ ] Identification of the body.
- [ ] ...  