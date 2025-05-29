import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm


from dataclasses import dataclass
from IPython.display import display
from ipywidgets import GridspecLayout, Layout
from scipy.odr import Model, RealData, ODR
from scipy.stats import t


try:
    from pyCompare import blandAltman
except ModuleNotFoundError:
    import subprocess
    subprocess.run(["pip", "install", "pyCompare", "--quiet"], check=True)
    from pyCompare import blandAltman


@dataclass
class BlandAltman:
    x_input: list
    y_input: list

    def plot(self):
        X = np.mean(self.x_input, axis=1)
        Y = np.mean(self.y_input, axis=1)

        blandAltman(Y, X, confidenceInterval=None)
        plt.show()


@dataclass
class WLSRegresi:
    x_input: list
    y_input: list

    def cetak(self):
        X = np.mean(self.x_input, axis=1)
        Y = np.mean(self.y_input, axis=1)

        sd_Y = np.std(self.y_input, axis=1, ddof=1)
        pemberat = 1 / sd_Y

        X = sm.add_constant(X)
        model = sm.WLS(Y, X, weights=pemberat)
        results = model.fit()

        print(results.summary())


@dataclass
class WDRegresi:
    x_input: list
    y_input: list

    def fungsi_linear(beta, x):
        return beta[0] + beta[1] * x

    def cetak(self):
        X = np.mean(self.x_input, axis=1)
        Y = np.mean(self.y_input, axis=1)

        sd_x = np.std(self.x_input, axis=1, ddof=1)
        sd_y = np.std(self.y_input, axis=1, ddof=1)

        model = Model(WDRegresi.fungsi_linear)
        data = RealData(X, Y, sx=sd_x, sy=sd_y)
        odr = ODR(data, model, beta0=[0, 1])

        hasil = odr.run()
        
        beta = hasil.beta
        se_beta = hasil.sd_beta
        df = len(X) - len(beta)
        t_stat = t.ppf(1 - 0.05 / 2, df)

        bawah = beta - t_stat * se_beta
        atas = beta + t_stat * se_beta

        print(f'Persamaan regresi: y = {beta[0]:.4f} + {beta[1]:.4f}x')
        print(f'95% CI Kecerunan: {bawah[1]:.4f} , {atas[1]:.4f}')
        print(f'95% CI Pintasan: {bawah[0]:.4f} , {atas[0]:.4f}')


@dataclass
class Grid:
    gridS: GridspecLayout = None
    gridO: widgets.Output = None
    baris: int = 1
    lajur: int = 3

    def __post_init__(self):
        self.wj_data = []

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

        self.wj_data = []

        with self.gridO:
            self.gridO.clear_output(wait=True)
            self.gridD = GridspecLayout(bil_n + 1, jum_lajur, layout=Layout(width="100%"))

            for i in range(bil_n + 1):
                baris_wj = []
                for j in range(jum_lajur):
                    if i==0 and j==0:
                        wj = widgets.Label(value="Data", layout=Layout(width=f'{lebar}px'))
                    elif i==0 and j<(bil_x + 1):
                        wj = widgets.Label(value=f"x{j}", layout=Layout(width=f'{lebar}px'))
                    elif i==0 and j>bil_x:
                        wj = widgets.Label(value=f"y{j-bil_x}", layout=Layout(width=f'{lebar}px'))
                    elif j==0:
                        wj = widgets.Label(value=f"S{i}", layout=Layout(width=f'{lebar}px'))
                    else:
                        wj = widgets.FloatText(
                            value=0.,
                            disabled=False,
                            layout=Layout(width=f'{lebar}px'),
                        )

                        baris_wj.append(wj)

                    self.gridD[i,j] = wj

                if i>0:
                    self.wj_data.append(baris_wj)

            display(self.gridD)

    def ambilData(self):
        data = {
            "x": [],
            "y": []
        }

        if not self.wj_data:
            return data

        bil_x = self.gridS[0,1].value

        for baris in self.wj_data:
            nilai_x = [w.value for w in baris[:bil_x]]
            nilai_y = [w.value for w in baris[bil_x:]]

            data["x"].append(nilai_x)
            data["y"].append(nilai_y)

        return data
