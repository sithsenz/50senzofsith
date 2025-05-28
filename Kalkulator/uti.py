import ipywidgets as widgets
import matplotlib.pyplot as plt


from dataclasses import dataclass
from IPython.display import display
from ipywidgets import GridspecLayout, Layout


try:
    from pyCompare import blandAltman
except ModuleNotFoundError:
    import subprocess
    subprocess.run(["pip", "install", "pyCompare", "--quiet"], check=True)
    from pyCompare import blandAltman


@dataclass
class BlandAltman():
    x_input: str
    y_input: str
    ralat: str = f'''
⚠️ Ralat input! Sila semak semula format data anda. Pastikan:
- Nombor dipisahkan dengan koma (cth: 4.5, 5.0, 4.8)
- Tiada huruf atau simbol lain
- Tiada koma berlebihan
'''

    def plot(self):
        try:
            X, Y = [], []

            for x in self.x_input.split(','):
                if x.strip():
                    X.append(float(x.strip()))

            for y in self.y_input.split(','):
                if y.strip():
                    Y.append(float(y.strip()))
            
            mesej: str = f'''
⚠️ Ralat input! Bilangan data x_input dan y_input harus sama.
x_input mengandungi {len(X)} data, manakala
y_input mengandungi {len(Y)} data.
'''

            if len(X) != len(Y):
                raise ValueError(mesej)
            
            blandAltman(Y, X, confidenceInterval=None)
            plt.show()

        except ValueError as ve:
            if "could not convert string to float" in str(ve):
                print(self.ralat)
            
            print(ve)
        except Exception:
            print(self.ralat)


@dataclass
class Wijet():
    jenis: str
    label: str
    lebar: str

    def baharu(self):
        if self.jenis=="teks":
            wj = widgets.Text(
                value=self.label,
                disabled=True,
                layout=Layout(width=self.lebar),
            )
        elif self.jenis=="integer":
            wj = widgets.IntText(
                value=0,
                disabled=False,
                layout=Layout(width=self.lebar),
            )
        elif self.jenis=="angka":
            wj = widgets.FloatText(
                value=0.,
                disabled=False,
                layout=Layout(width=self.lebar),
            )
    
        return wj


@dataclass
class Grid():
    baris: int = 1
    lajur: int = 3

    def sampel(self):
        grid = GridspecLayout(self.baris, self.lajur, layout=Layout(width='100%'))
        
        label = ["bil n", "bil x", "bil y"]

        for j, t in enumerate(label):
            grid[0,j] = widgets.IntText(
                value=1,
                description=t,
                disabled=False,
                layout=Layout(width='200px'),
            )
        
        return grid
