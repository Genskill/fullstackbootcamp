'use strict';

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false}; 
  }

  render() {
    if (this.state.liked) {
        return "You clicked like";
      } else {
          return (<button onClick={() => this.setState({ liked: true })}>
                  Like
                  </button>);
      }
  }
}

const rdemo = document.querySelector("#rdemo");
ReactDOM.render(React.createElement(LikeButton), rdemo);
