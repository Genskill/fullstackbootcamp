'use strict';

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

      return React.createElement(
          'button',
          { onClick: () => this.setState({ liked: true }) },
          'Like'
      );
  }
}

const rdemo = document.querySelector("#rdemo");
ReactDOM.render(React.createElement(LikeButton), rdemo);
