from dataclasses import dataclass
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
            x_input = self.x_input
            y_input = self.y_input
            
            X = [float(x.strip()) for x in x_input.split(',')]
            
            Y = [float(y.strip()) for y in y_input.split(',')]
            
            mesej: str = f'Bilangan data x_input dan y_input harus sama. x_input mengandungi {len(X)} data, manakala y_input mengandungi {len(Y)} data.'

            assert len(X) == len(Y)
            
            blandAltman(Y, X, confidenceInterval=None)
        except AssertionError:
            print(mesej)
        except Exception:
            print(ralat)
