# ----------------------------------------------------
# SPDX-FileCopyrightText: AsFigo Technologies, UK
# SPDX-FileCopyrightText: VerifWorks, India
# SPDX-License-Identifier: MIT
# ----------------------------------------------------
'''
import sys
import os
import argparse
# Add the 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import logging
import verible_verilog_syntax
from ..af_lint_rule import AsFigoLintRule
from asfigo_linter import AsFigoLinter
from afsvalint.rules.af_asrt_no_label import MissingLabelChk
from afsvalint.rules.af_perf_no_pass_ablk import PerfNoPABlk
from afsvalint.rules.af_no_timeliteral import NoExplTimeLiterals
from afsvalint.rules.af_no_within_oper import NoWithinOperInAsrt
from afsvalint.rules.af_no_fmatch_oper import NoFirstMatchOperInAsrt
from afsvalint.rules.af_no_range_ant import NoRangeInAntAsrt
from afsvalint.rules.af_perf_no_ub_range_ant import NoUBRangeInAntAsrt
from afsvalint.rules.af_func_missing_fablk import FuncMissingFABLK
from afsvalint.rules.af_missing_elbl_prop import MissingEndLblProp
from afsvalint.rules.af_missing_elbl_seq import MissingEndLblSEQ
from afsvalint.rules.af_prop_naming import PropNaming
from afsvalint.rules.af_perf_missing_impl_oper import MissingImplicationOper
from afsvalint.rules.af_perf_no_large_del import NoLargeDelayProp
from afsvalint.rules.af_use_simple_cnseq import UseSimpleExprConseq
from afsvalint.rules.af_no_dollar_time import UseRealTimeVsTime
from afsvalint.rules.af_func_cov_nolap import FuncNOLAPInCoverProp 
from afsvalint.rules.af_func_cov_olap import FuncOLAPInCoverProp 
from afsvalint.rules.af_reuse_fa_one_liner import ReuseNoOneLinerFABLK 
from afsvalint.rules.af_func_no_ub_in_cnseq import NoUBRangeInConseqAsrt 
from afsvalint.rules.af_asrt_naming import AssertNaming
from afsvalint.rules.af_no_aa_exists_sva import AvoidAAExistsSVA
from afsvalint.rules.af_no_pop_back_sva import AvoidPopBkSVA
from afsvalint.rules.af_no_pop_front_sva import AvoidPopFrSVA
from afsvalint.rules.af_assume_naming import AssumeNaming
from afsvalint.rules.af_cover_naming import CoverNaming

class SVALinter(AsFigoLinter):
    """Linter that applies multiple rules on SVA code"""

    def __init__(self, configFile, logLevel=logging.INFO):
        super().__init__(configFile=configFile, logLevel=logLevel)
        # Automatically discover and register all subclasses of AsFigoLintRule
        self.rules = [rule_cls(self) for rule_cls in AsFigoLintRule.__subclasses__()]

    def loadSyntaxTree(self):
        """Loads Verilog syntax tree using VeribleVerilogSyntax."""
        parser = verible_verilog_syntax.VeribleVerilogSyntax()
        return parser.parse_files([self.testName], options={"gen_tree": True})

    def runLinter(self):
        """Runs all registered lint rules on the Verilog file."""
        treeData = self.loadSyntaxTree()

        for filePath, fileData in treeData.items():
            self.logInfo("SVALint", f"Loaded test file: {self.testName}")
            
            for rule in self.rules:
                rule.run(filePath, fileData)

            self.logSummary()


def main():
    byolDemo = SVALinter(configFile="config.toml", logLevel=logging.INFO)
    byolDemo.runLinter()

if __name__ == "__main__":
    main()

def main():
    parser = argparse.ArgumentParser(description="Run SVALint linter")
    parser.add_argument("--config", default="config.toml", help="Path to config file")
    args = parser.parse_args()

    linter = SVALinter(configFile=args.config, logLevel=logging.INFO)
    linter.runLinter()
if __name__ == "__main__":
    main()

'''
import argparse
import logging
import sys

from . import verible_verilog_syntax
from .asfigo_linter import AsFigoLinter
from .af_lint_rule import AsFigoLintRule

# Import all rules
from afsvalint.rules.af_asrt_no_label import MissingLabelChk
from afsvalint.rules.af_no_pop_back_sva import AvoidPopBkSVA
from afsvalint.rules.af_assume_naming import AssumeNaming
from afsvalint.rules.af_perf_no_ub_range_ant import NoUBRangeInAntAsrt
from afsvalint.rules.af_no_within_oper import NoWithinOperInAsrt
from afsvalint.rules.af_func_cov_olap import FuncOLAPInCoverProp
from afsvalint.rules.af_func_missing_fablk import FuncMissingFABLK
from afsvalint.rules.af_no_fmatch_oper import NoFirstMatchOperInAsrt
from afsvalint.rules.af_reuse_fa_one_liner import ReuseNoOneLinerFABLK
from afsvalint.rules.af_missing_elbl_seq import MissingEndLblSEQ
from afsvalint.rules.af_func_no_ub_in_cnseq import NoUBRangeInConseqAsrt
from afsvalint.rules.af_no_timeliteral import NoExplTimeLiterals
from afsvalint.rules.af_prop_naming import PropNaming
from afsvalint.rules.af_perf_missing_impl_oper import MissingImplicationOper
from afsvalint.rules.af_missing_elbl_prop import MissingEndLblProp
from afsvalint.rules.af_no_range_ant import NoRangeInAntAsrt
from afsvalint.rules.af_no_dollar_time import UseRealTimeVsTime
from afsvalint.rules.af_perf_no_pass_ablk import PerfNoPABlk
from afsvalint.rules.af_use_simple_cnseq import UseSimpleExprConseq
from afsvalint.rules.af_perf_no_large_del import NoLargeDelayProp
from afsvalint.rules.af_func_cov_nolap import FuncNOLAPInCoverProp
from afsvalint.rules.af_cover_naming import CoverNaming
from afsvalint.rules.af_no_aa_exists_sva import AvoidAAExistsSVA
from afsvalint.rules.af_asrt_naming import AssertNaming
from afsvalint.rules.af_no_pop_front_sva import AvoidPopFrSVA

class SVALinter(AsFigoLinter):
    """Linter that applies multiple rules on SVA/SystemVerilog code"""

    def __init__(self, file_path, configFile="config.toml", logLevel=logging.INFO):
        super().__init__(file_path=file_path, configFile=configFile, logLevel=logLevel)
        #self.testName = file_path
        self.rules = [rule_cls(self) for rule_cls in AsFigoLintRule.__subclasses__()]


    def loadSyntaxTree(self):
        """Load Verilog syntax tree using VeribleVerilogSyntax"""
        parser = verible_verilog_syntax.VeribleVerilogSyntax()
        try:
            # parse the file as a single string
            with open(self.testName, "r") as f:
                code = f.read()
            tree = parser.parse_string(code, options={"gen_tree": True})
            return {self.testName: tree}
        except FileNotFoundError:
            logging.error(f"File not found: {self.testName}")
            sys.exit(1)
        except Exception as e:
            logging.error(f"Parsing failed: {e}")
            sys.exit(1)

    def runLinter(self):
        """Run all registered lint rules on the Verilog file"""
        treeData = self.loadSyntaxTree()

        for filePath, fileData in treeData.items():
            self.logInfo("SVALint", f"Loaded test file: {filePath}")

            for rule in self.rules:
                rule.run(filePath, fileData)

            self.logSummary()


def parse_args():
    parser = argparse.ArgumentParser(description="Run SVALint linter")
    parser.add_argument(
        "file",
        help="Path to SystemVerilog (.sv) file to lint"
    )
    parser.add_argument(
        "--config", "-c",
        default="config.toml",
        help="Path to configuration file (optional)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")

    linter = SVALinter(file_path=args.file, configFile=args.config, logLevel=log_level)
    linter.runLinter()


if __name__ == "__main__":
    main()
