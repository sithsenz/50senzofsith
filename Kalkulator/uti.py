from dataclasses import dataclass
import matplotlib.pyplot as plt


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
                if x.strip() := a:
                    X.append(float(a))

            for y in self.y_input.split(','):
                if y.strip() := b:
                    Y.append(float(b))
            
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
