import palette

class palette(palette.palette):

  def __init__(self):

    self.__source__ = 'barnes'

    self.__colours__ = {
      "#71d5f8": {
          "name": "skyblue"
      },
      "#3c7cf6": {
          "name": "ultramarine"
      },
      '#0f48af': {
        "name": "mediumblue"
      },
      '#192a72': {
        "name": "darkblue"
      },
      '#211346': {
        "name": "violet"
      },
      '#0e4349': {
        "name": "teal"
      },
      '#0f4223': {
        "name": "green"
      },
      '#58871f': {
        "name": "leafgreen"
      },
      '#9ac12d': {
        "name": "lightgreen"
      },
      '#fffc23': {
        "name": "yellow"
      },
      '#e69c17': {
        "name": "orange"
      },
      '#eb6915': {
        "name": "darkorange"
      },
      '#d8440e': {
        "name": "vermilion"
      },
      '#cd130e': {
        "name": "red"
      },
      '#9d3469': {
        "name": "fuchsia"
      },
      '#6b2056': {
        "name": "purple"
      },
      '#541439': {
        "name": "darkpurple"
      },
      '#6e6e6e': {
        "name": "darkgrey"
      },
      '#dcdcdc': {
        "name": "lightgrey"
      },
      '#f0f0f0': {
        "name": "palegrey"
      }
    }

if __name__ == '__main__':

    c = colours()

    print c.source()
    print c.hex('palegrey')
    print c.name('#f0f0f0')
