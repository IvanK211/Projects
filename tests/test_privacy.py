"""Scanner fixtures are assembled from harmless parts; no real secret values."""
import sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from privacy_scan import inspect_text,scan
from repository_files import candidates
class PrivacyTests(unittest.TestCase):
    def test_documentation_values_allowed(self):self.assertEqual(inspect_text('192.0.2.10 user@example.invalid 127.0.0.1'),[])
    def test_non_example_email(self):
        text='synthetic-user'+'@'+'synthetic-domain.invalid'
        self.assertIn((1,'non-example-email'),inspect_text(text))
    def test_private_range_flagged(self):
        text='.'.join(['10','1','2','3'])
        self.assertIn((1,'non-documentation-ipv4'),inspect_text(text))
    def test_token_flagged(self):
        text='glpat'+'-'+'Z'*24
        self.assertIn((1,'gitlab-token'),inspect_text(text))
    def test_url_credential_flagged(self):
        text='https'+'://'+'u'+':'+'p'+'@'+'example.invalid/'
        self.assertIn((1,'url-credentials'),inspect_text(text))
    def test_ignored_outputs_not_packaged(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);(root/'local-output').mkdir();(root/'local-output'/'private.json').write_text('{}');(root/'README.md').write_text('# Example')
            self.assertEqual([p.name for p in candidates(root)],['README.md'])
    def test_binary_unreviewed_type_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);(root/'archive.zip').write_bytes(b'not a real archive')
            with self.assertRaises(ValueError):list(candidates(root))
    def test_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);(root/'README.md').write_text('Example')
            try:(root/'alias.md').symlink_to(root/'README.md')
            except OSError:self.skipTest('Symlinks unavailable')
            with self.assertRaises(ValueError):list(candidates(root))
if __name__=='__main__':unittest.main()
