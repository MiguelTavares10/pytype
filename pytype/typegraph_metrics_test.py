"""Basic tests for accessing typegraph metrics from Python."""
import textwrap

from pytype import context
from pytype import typegraph
from pytype.tests import test_base


class MetricsTest(test_base.BaseTest):

  def setUp(self):
    super().setUp()
    self.ctx = context.Context(options=self.options, loader=self.loader)

  def run_program(self, src):
    return self.ctx.vm.run_program(textwrap.dedent(src), "", maximum_depth=10)

  def assertNotEmpty(self, container, msg=None):
    if not container:
      msg = msg or "{!r} has length of 0.".format(container)
      self.fail(msg=msg)

  def test_basics(self):
    self.run_program("""
        def foo(x: str) -> int:
          return x + 1
        a = foo(1)
    """)
    metrics = self.ctx.program.calculate_metrics()
    # No specific numbers are used to prevent this from being a change detector.
    self.assertIsInstance(metrics, typegraph.cfg.Metrics)
    self.assertGreater(metrics.binding_count, 0)
    self.assertNotEmpty(metrics.cfg_node_metrics)
    self.assertNotEmpty(metrics.variable_metrics)
    self.assertNotEmpty(metrics.solver_metrics)
    self.assertNotEmpty(metrics.solver_metrics[0].query_metrics)


if __name__ == "__main__":
  test_base.main()
