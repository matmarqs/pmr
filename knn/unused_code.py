def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.1f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct


def pie(x, title='', cmap='bwr', fontsize=14,
        func=lambda x: x*x, show=True):
    fig, ax = plt.subplots()
    ax.set_title(title, fontsize=fontsize)
    n =  x.to_numpy()
    n_norm = n/n.max()
    fracs = func(n_norm)
    ax.pie(x, autopct=make_autopct(x), shadow=True, labels=x.index,
           startangle=90, explode=0.1*n_norm)
    patches = ax.patches
    norm = colors.Normalize(0, 1)
    cm = plt.cm.get_cmap(name=cmap)
    for frac, patch in zip(fracs, patches):
        color = cm(norm(frac))
        patch.set_facecolor(color)
    if show:
        plt.show()
