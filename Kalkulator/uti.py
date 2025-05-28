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
class Grid():
    gridS: GridspecLayout = None
    gridO: widgets.Output = None
    baris: int = 1
    lajur: int = 3


    def sampel(self):
        grid = GridspecLayout(self.baris, self.lajur, layout=Layout(width="100%"))
        
        label = ["bil n", "bil x", "bil y"]

        for j, t in enumerate(label):
            grid[0,j] = widgets.BoundedIntText(
                min=1,
                value=1,
                description=t,
                disabled=False,
                layout=Layout(width="200px"),
            )
        
        return grid
    
    def data(self, change=None):
        bil_n = self.gridS[0,0].value
        bil_x = self.gridS[0,1].value
        bil_y = self.gridS[0,2].value
        jum_lajur = bil_x + bil_y + 1

        lebar = 1000 // jum_lajur

        with self.gridO:
            self.gridO.clear_output(wait=True)
            self.gridD = GridspecLayout(bil_n + 1, jum_lajur, layout=Layout(width="100%"))

            for i in range(bil_n + 1):
                for j in range(jum_lajur):
                    if i==0 and j==0:
                        self.gridD[i,j] = widgets.Label(value="Data", layout=Layout(width="100px"))
                    elif i==0 and j<(bil_x + 1):
                        self.gridD[i,j] = widgets.Label(value=f"x{j}", layout=Layout(width=f'{lebar}px'))
                    elif i==0 and j>bil_x:
                        self.gridD[i,j] = widgets.Label(value=f"y{j-bil_x}", layout=Layout(width=f'{lebar}px'))
                    elif j==0:
                        self.gridD[i,j] = widgets.Label(value=f"S{i}", layout=Layout(width=f"100px"))
                    else:
                        self.gridD[i,j] = widgets.FloatText(
                            value=0.,
                            disabled=False,
                            layout=Layout(width=f'{lebar}px'),
                        )
            
            display(self.gridD)
