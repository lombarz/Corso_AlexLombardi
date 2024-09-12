#Create 2 script:
# 1) semplicemente inserisce tre paragrafi in un file (fonte possibile: https://it.lipsum.com/);
# 2) Leggete il file e stampate il numero di parole, di righe e di caratteri

stringa = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce et turpis sed massa mollis mattis. Praesent a placerat massa. Cras consectetur fermentum elit vitae mattis. Suspendisse fermentum, nisi nec interdum iaculis, elit nulla suscipit arcu, sed hendrerit quam elit sed ligula. Nullam feugiat eros non est suscipit gravida. Nullam a orci sollicitudin, dapibus felis ut, tempus nisi. Vivamus auctor scelerisque facilisis. Maecenas nec risus nulla. Donec augue arcu, lobortis in elit vitae, tristique varius lacus. Aenean interdum a neque eu molestie. Etiam vel tincidunt arcu. Nulla facilisis turpis tempor sodales fermentum. Donec venenatis non ipsum et hendrerit. Vestibulum lobortis vel ipsum sed mollis.
Donec diam mauris, venenatis in diam et, vulputate volutpat odio. Praesent risus ex, hendrerit eget fringilla non, elementum vel erat. Nulla facilisi. Ut convallis libero leo, nec sodales dui sagittis ac. Mauris quis suscipit ipsum. Praesent vestibulum, velit eu pharetra egestas, orci nulla efficitur tellus, eget fringilla mauris ipsum sed eros. Maecenas bibendum leo ut bibendum hendrerit. Aliquam posuere diam ligula. Vestibulum tempor arcu magna, sit amet maximus lectus vehicula nec. In quam ex, ullamcorper vitae scelerisque id, lacinia a eros. Ut sit amet elit metus. Ut finibus dolor vitae pellentesque aliquam. In fermentum erat felis, et porta tellus laoreet consequat. Phasellus rutrum placerat metus non viverra.
Nulla et nunc eu eros placerat hendrerit. Duis ex arcu, egestas nec tellus non, imperdiet aliquam sem. Maecenas dolor enim, consectetur sed ultrices eget, auctor eget justo. Praesent ornare sodales maximus. Aliquam erat volutpat. Maecenas tristique suscipit enim. Mauris at egestas massa. In sit amet enim enim. Donec et metus id libero efficitur accumsan in sed odio. Integer lectus erat, efficitur vel est vel, tristique malesuada mi. In magna arcu, dignissim quis nulla ut, laoreet lobortis nulla. Sed in purus rhoncus, imperdiet orci eget, rutrum sapien. Ut venenatis auctor efficitur. Vivamus quis tellus id nulla faucibus convallis ut in elit. Nullam vestibulum magna sit amet mi congue, a fringilla libero varius."""

with open('testo.txt',"w") as f:
    f.write(stringa)


def lettura(file):
    with open(file,'r') as f:
        return f.read()
    
contenuto = lettura('testo.txt')

stringa_paragrafi = contenuto.split('\n')

print("I paragrafi sono: ",len(stringa_paragrafi))

s = contenuto.split(' ')

print("I caratteri spazi inclusi sono: ",len(contenuto))

count = 0
for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j] != '\n':
            count+=1
print("I caratteri spazi esclusi sono: ",count)

    







